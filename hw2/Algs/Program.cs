using System;
using System.Collections.Generic;
using System.Linq;

namespace HW2
{
    class FourthTaskSolver
    {
        private const int veryBigPrice = 100000000;

        private static List<int> InputLine()
        {
            return Console.ReadLine().Split().Select(int.Parse).ToList();
        }

        public static (List<List<int>>, List<Dictionary<int, HashSet<int>>>) Input()
        {
            var countByType = InputLine();

            var allPrices = new List<List<int>>();
                      
            for (var i = 0; i < 4; i++)
            {
                var prices = InputLine();
                allPrices.Add(prices);
            }

            var allNoMathichgComps = new List<Dictionary<int, HashSet<int>>>();

            for (var i = 0; i < 3; i++)
            {
                var count = int.Parse(Console.ReadLine());
                var nmForType = new Dictionary<int, HashSet<int>>();

                for (var j = 0; j < countByType[i]; j++)
                    nmForType[j] = new HashSet<int>();                
                
                for (var nmCompsIndex = 0; nmCompsIndex < count; nmCompsIndex++)
                {
                    var line = InputLine();
                    var first = line[0];
                    var second = line[1];
                    if (!nmForType.ContainsKey(second - 1))
                        nmForType[second - 1] = new HashSet<int>();
                    nmForType[second - 1].Add(first - 1);
                }
                allNoMathichgComps.Add(nmForType);
            }

            return (allPrices, allNoMathichgComps);
        }

        public static void GetCheapestComp(List<List<int>> prices, List<Dictionary<int, HashSet<int>>> nmComps)
        {
            var bests = new List<List<int>> { prices[0] };

            for (var i = 1; i < 4; i++)
            {
                var temp = new List<int>();
                for (var j = 0; j < prices[i].Count; j++)
                {
                    temp.Add(veryBigPrice);
                }
                bests.Add(temp);
            }

            for (var componentType = 1; componentType < 4; componentType++)
            {
                var pricesByType = prices[componentType];
                var nmForType = nmComps[componentType - 1];

                var previousBests = bests[componentType - 1];
                var typesBest = bests[componentType];

                var typeCount = pricesByType.Count;
                var previousCompTypeCount = previousBests.Count;

                var indexByCostAscending = GetSortedOrder(previousBests);

                for (var compInd = 0; compInd < typeCount; compInd++)
                {
                    var price = pricesByType[compInd];
                    var nmForComp = nmForType[compInd];

                    for (var prevConpInd = 0; prevConpInd < previousCompTypeCount; prevConpInd++)
                    {
                        var well = !nmForComp.Contains(indexByCostAscending[prevConpInd]);
                    
                        if (well)
                        {
                            typesBest[compInd] = price + previousBests[indexByCostAscending[prevConpInd]];
                            break;
                        }
                    }
                }
                
            } 
            
            Console.WriteLine(bests[^1].Where(cost => Math.Abs(cost) < veryBigPrice).DefaultIfEmpty(-1).Min());                  
        }

        private static List<int> GetSortedOrder(List<int> list)
        {
            return list.Select((el, ind) => Tuple.Create(el, ind)).OrderBy(x => x).Select(x => x.Item2).ToList();
        }
    }

    class Program
    {
        public static void Main()
        {
            var (prices, noMatching) = FourthTaskSolver.Input();
            FourthTaskSolver.GetCheapestComp(prices, noMatching);
        }
    }
}