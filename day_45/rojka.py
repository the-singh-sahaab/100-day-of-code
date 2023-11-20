class Solution:
    def garbageCollection(self, grabage: List[str], travel: List[int]) -> int:
        g = 0
        g_count = 0
        p = 0
        p_count = 0
        m = 0
        m_count = 0
        for i in range(len(grabage)):
            if "G" in grabage[i]:
                g = i
                g_count += grabage[i].count("G")
            if "M" in grabage[i]:
                m = i
                m_count += grabage[i].count("M")
            if "P" in grabage[i]:
                p = i
                p_count += grabage[i].count("P")

        glass = g_count + sum(travel[:g])
        metal = m_count + sum(travel[:m])
        paper = p_count + sum(travel[:p])
        return glass + paper + metal
