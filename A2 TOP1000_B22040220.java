package Top1000Numbers;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

public class Top1000Numbers {

    public static void main(String[] args) {
        // 读取文件并将所有数字存储在列表中
        List<Integer> numbers = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader("data2.txt"))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] nums = line.trim().split("\\s+"); // 以空格分隔数字
                for (String num : nums) {
                    numbers.add(Integer.parseInt(num)); // 将字符串转换为整数并添加到列表
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // 找出前1000个最大的数字
        List<Integer> top1000Numbers = findTop1000(numbers);
        // 打印结果
        System.out.println(top1000Numbers);
    }

    // 主要方法：找出前1000个最大的数字
    public static List<Integer> findTop1000(List<Integer> numbers) {
        int numSubsets = 100; // 子集的数量
        int subsetSize = numbers.size() / numSubsets; // 每个子集的大小
        List<List<Integer>> subsets = new ArrayList<>(); // 存储所有子集

        // 将数据分割成多个子集
        for (int i = 0; i < numSubsets; i++) {
            int start = i * subsetSize;
            int end = (i + 1) * subsetSize;
            if (i == numSubsets - 1) {
                end = numbers.size(); // 最后一个子集包括所有剩余元素
            }
            subsets.add(new ArrayList<>(numbers.subList(start, end))); // 创建子集并添加到列表
        }

        List<List<Integer>> top1000InSubsets = new ArrayList<>(); // 存储每个子集的前1000个最大数字
        for (List<Integer> subset : subsets) {
            top1000InSubsets.add(findTop1000InSubset(subset)); // 找出每个子集的前1000个最大数字
        }

        return mergeTop1000(top1000InSubsets); // 合并所有子集的结果
    }

    // 在单个子集中找出前1000个最大的数字
    private static List<Integer> findTop1000InSubset(List<Integer> subset) {
        if (subset.size() <= 1000) {
            return subset.stream().sorted(Collections.reverseOrder()).limit(1000).collect(Collectors.toList()); // 如果子集大小小于等于1000，直接排序
        }

        PriorityQueue<Integer> minHeap = new PriorityQueue<>(1000); // 创建最小堆，存储前1000个最大数字
        for (Integer number : subset) {
            if (minHeap.size() < 1000) {
                minHeap.offer(number); // 堆中元素少于1000，直接添加
            } else if (number > minHeap.peek()) {
                minHeap.poll(); // 当前数字大于堆顶元素，替换堆顶元素
                minHeap.offer(number);
            }
        }

        return new ArrayList<>(minHeap); // 返回堆中的元素
    }

    // 合并所有子集的结果，找出前1000个最大的数字
    private static List<Integer> mergeTop1000(List<List<Integer>> results) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(1000); // 创建最小堆，存储前1000个最大数字
        for (List<Integer> result : results) {
            for (Integer number : result) {
                if (minHeap.size() < 1000) {
                    minHeap.offer(number); // 堆中元素少于1000，直接添加
                } else if (number > minHeap.peek()) {
                    minHeap.poll(); // 当前数字大于堆顶元素，替换堆顶元素
                    minHeap.offer(number);
                }
            }
        }

        return new ArrayList<>(minHeap); // 返回堆中的元素
    }
}