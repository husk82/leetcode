public class bestTimeToBuy121 {

    public int maxProfit(int[] prices) {
        int left = 0;
        int right = 1;
        int max = 0;
        int profit = 0;

        while (left < prices.length && right < prices.length) {

            if (prices[left] < prices[right]) {
                profit = prices[right] - prices[left];
                max = Math.max(max, profit);
            }
            else {
                left = right;
            }
            right++;
        }
        return max;
    }
}
