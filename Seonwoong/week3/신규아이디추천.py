def solution(new_id):
    
    new_id = new_id.lower()
    allowed_characters = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    new_id = ''.join(c for c in new_id if c in allowed_characters)
    
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    new_id = new_id.strip('.')

    if not new_id: new_id = 'a'
    
    if len(new_id)>15: 
        new_id=new_id[:15]
    
    new_id = new_id.rstrip('.')
    
 
    while len(new_id)<3:
         new_id+=new_id[-1]
    
    return new_id
