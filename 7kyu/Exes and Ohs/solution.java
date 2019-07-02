public class XO{
  
  public static boolean getXO (String str) {
    
    // Good Luck!!
    int x_cnt = 0;
    int o_cnt = 0;
    
    str = str.toLowerCase();
    System.out.println(str);
    for (int i = 0; i < str.length(); i++) {
        if (str.charAt(i) == 'x') 
            x_cnt++;
        else if(str.charAt(i) == 'o')
            o_cnt++;
    }
    System.out.println(x_cnt);
    System.out.println(o_cnt);
    if(x_cnt == o_cnt)
      return true;
    return false;
  }
}
