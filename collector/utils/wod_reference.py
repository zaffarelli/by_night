'''
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      

'''
from collector.models.chronicles import Chronicle

def get_current_chronicle():
  #current_chronicle = Chronicle.objects.get(is_current=True)
  current_chronicle = Chronicle.objects.filter(is_current=True).first()
  return current_chronicle
  
