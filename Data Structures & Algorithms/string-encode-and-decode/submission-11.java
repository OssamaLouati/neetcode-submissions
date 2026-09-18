class Solution {

    public String encode(List<String> strs) {
        if (strs.size() == 0) return null;
        if (strs.size() == 1) {
            if (strs.get(0).equals("")) return "";
            return strs.get(0);
        }

        StringBuilder sb = new StringBuilder();
        String delimiter = "∂";
        for (String str: strs) {
            sb.append(str).append(delimiter);
        }

        return sb.toString();
    }

    public List<String> decode(String str) {
        if (str == null) return new ArrayList<>();
        if (str.equals("")) {
            return List.of("");
        } 
        String delimiter = "∂";

        List<String> decoded_strs = new ArrayList<>(Arrays.asList(str.split(delimiter, -1)));
        if (decoded_strs.size()==1) return decoded_strs;
        decoded_strs.remove(decoded_strs.size()-1);
        return decoded_strs;
    }
}
