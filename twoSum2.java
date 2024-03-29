import java.util.*;
public class twoSum2 {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode l3 = new ListNode(0);
        ListNode cur = l3, p=l1, q=l2;
        int carry = 0;
        int sum = 0;
        while (p != null || q != null){
            int x = (p!=null) ? p.val : 0;
            int y = (q!=null) ? q.val : 0;
            sum = x + y + carry;
            carry = sum / 10;
            cur.next = new ListNode(sum%10);
            cur = cur.next;
            if (q != null) q = q.next;
            if (p != null) p = p.next;
        }
        if (carry>0){
            cur.next = new ListNode(carry);
        }
        return l3.next;
    }
}
