package org.example;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

/**
 * 这个类用于找出分数最高的前10个数。
 */
public class TopTenScores {
    public TopTenScores() {
    }

    /**
     * 程序的主入口点。
     */
    public static void main(String[] args) {
        // 从文件中读取分数并存入数组
        int[] scores = readScoresFromTextFile("data2.txt");
        // 找出分数最高的前10个数
        int[] top10Scores = findTop10(scores);
        // 打印结果
        for (int score : top10Scores) {
            System.out.println(score);
        }
    }

    /**
     * 从文本文件中读取分数。
     */
    private static int[] readScoresFromTextFile(String filename) {
        List<Integer> scoreList = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] scoreStrings = line.trim().split("\\s+");//数字以空格分隔
                for (String scoreString : scoreStrings) {
                    scoreList.add(Integer.parseInt(scoreString)); // 将字符串转换为整数并添加到列表
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        // 将列表转换为数组并返回
        return scoreList.stream().mapToInt(Integer::intValue).toArray(); // 使用stream将ArrayList转换为int数组
    }

    /**
     * 找出数组中分数最高的前10个数。
     * @param scores 包含所有分数的整型数组。
     * @return 包含前10个最高分数的整型数组。
     */
    public static int[] findTop10(int[] scores) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();
        int i = scores.length;

        // 使用优先队列（最小堆）来找出前10个最高分数
        for (int var4 = 0; var4 < i; ++var4) {
            int score = scores[var4];
            if (minHeap.size() < 10) {
                minHeap.add(score); //堆未满直接加入
            } else if (score > minHeap.peek()) {
                minHeap.poll();          //堆满如果当前元素大于堆顶元素则替换
                minHeap.add(score);
            }
        }

        int[] top10 = new int[10];

        // 从优先队列中取出元素并逆序存储到数组中
        for (i = 9; i >= 0; --i) {
            top10[i] = minHeap.poll();
        }

        return top10;
    }
}