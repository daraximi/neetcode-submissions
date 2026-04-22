/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public boolean hasCycle(ListNode head) {
        HashSet<ListNode> seen = new HashSet<>();
        ListNode pointer = head;
        while (pointer != null){
            if(seen.contains(pointer)){
                return true;
            }else{
                seen.add(pointer);
            }
            pointer = pointer.next;
        }

        return false;
    }
}
