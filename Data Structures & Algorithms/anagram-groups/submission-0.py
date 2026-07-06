class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grupos = {}
        
        for palabra in strs:
            llave = "".join(sorted(palabra))
            if llave not in grupos:
                grupos[llave] = []
            grupos[llave].append(palabra)
        
        return list(grupos.values())