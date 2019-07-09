import java.util.*;
public class Dubstep {
  public static String SongDecoder (String song)
  {
     // Your code is here...
     System.out.println(song);
     String[] s = song.split("WUB");
     String str="";
     for(String i : s){
       System.out.println(i);
       str+=i+" ";
     }
     
     
     
     return str.replaceAll("\\s{2,}", " ").trim();
   }
}
