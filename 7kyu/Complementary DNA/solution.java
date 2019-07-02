public class DnaStrand {
  public static String makeComplement(String dna) {
    //Your code
    
    String x="";
    
    for (int i=0; i<dna.length(); i++){
      if(dna.charAt(i) == 'A')
        x+='T';
      else if(dna.charAt(i) == 'T')
        x+='A';
      else if(dna.charAt(i) == 'G')
        x+='C';
      else if (dna.charAt(i) == 'C')
        x+='G';
    }
    return(x);
  }
}
