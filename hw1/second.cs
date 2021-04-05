using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Numerics;

namespace algo_second
{
    internal class Program
    {

        public static void Main(string[] args)
        {
            var hash = long.Parse(Console.ReadLine());
            var module = 1000000000000159;
            for (int i = 65536; i < 131072; i++)
            {
                var binary = Convert.ToString(i, 2);
                long sum = 0;
                long root = 1;
                for (var j = binary.Length - 1; j > 0; j--)
                {
                    sum = (sum + binary[j] * root % module) % module;
                    root = root * 257 % module;
                }
                if (sum == hash)
                {
                    Console.WriteLine(binary.Substring(1));
                    Environment.Exit(0);
                }
            }
            Console.WriteLine("No");
        }
    }
}