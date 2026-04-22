class Solution {
    public boolean isValid(String s) {
        HashMap <String, String> checker = new HashMap<>();
        checker.put("]","[");
        checker.put("}","{");
        checker.put(")","(");
        ArrayList <String> stack = new ArrayList<>();

        for (int i = 0; i < s.length();i++){
            String character = String.valueOf(s.charAt(i));
            if (checker.containsKey(character)){
                if(stack.size()> 0 && stack.get(stack.size() - 1).equals(checker.get(character))){
                    stack.remove(stack.size()-1);
                }
                else{
                    return false;
                }
            }
            else{
                stack.add(character);
            }
        }
        return stack.size() == 0;
    }
}
