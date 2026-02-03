import math
import random

def generate_svg_outputs():
    # --- KONFIGURATION ---
    random.seed(42)
    n = 35
    width, height = 800, 450
    pts = [(random.uniform(50, width-50), random.uniform(50, height-50)) for _ in range(n)]

    # --- GRAFIK 1: GABRIEL SKELETON ---
    svg1 = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg1 += '<rect width="100%" height="100%" fill="#0a0a0a" />\n'
    
    for i in range(n):
        for j in range(i + 1, n):
            p1, p2 = pts[i], pts[j]
            mid = ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)
            r = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) / 2
            is_gabriel = True
            for k in range(n):
                if k == i or k == j: continue
                if math.sqrt((pts[k][0]-mid[0])**2 + (pts[k][1]-mid[1])**2) < r - 0.1:
                    is_gabriel = False; break
            if is_gabriel:
                svg1 += f'  <line x1="{p1[0]}" y1="{p1[1]}" x2="{p2[0]}" y2="{p2[1]}" stroke="#00ffcc" stroke-width="1.2" opacity="0.5" />\n'
    for p in pts:
        svg1 += f'  <circle cx="{p[0]}" cy="{p[1]}" r="3.5" fill="white" />\n'
    svg1 += '</svg>'

    # --- GRAFIK 2: COMPLEXITY CURVE ---
    svg2 = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">\n'
    svg2 += '<rect width="100%" height="100%" fill="#0a0a0a" />\n'
    # Achsen
    svg2 += '<line x1="50" y1="400" x2="750" y2="400" stroke="#888" stroke-width="2" />\n'
    svg2 += '<line x1="50" y1="400" x2="50" y2="50" stroke="#888" stroke-width="2" />\n'
    
    # Kurven (P-Klasse vs NP-Klasse Simulation)
    p_path = "M 50 400 "
    np_path = "M 50 400 "
    for x in range(0, 701, 20):
        real_x = 50 + x
        # P-Time: x^1.5 (skaliert)
        py = 400 - (x**1.2 / 5)
        p_path += f"L {real_x} {py} "
        # NP-Time: e^x (skaliert, explodiert schnell)
        if x < 250:
            npy = 400 - math.exp(x/40)
            np_path += f"L {real_x} {npy} "
    
    svg2 += f'<path d="{p_path}" fill="none" stroke="#00ffcc" stroke-width="3" />\n'
    svg2 += f'<path d="{np_path}" fill="none" stroke="#ff0055" stroke-width="3" stroke-dasharray="5,5" />\n'
    svg2 += '<text x="100" y="100" fill="#00ffcc" font-family="sans-serif" font-size="14">Skeletal Fixpoint (P)</text>\n'
    svg2 += '<text x="100" y="130" fill="#ff0055" font-family="sans-serif" font-size="14">Classical Search (NP)</text>\n'
    svg2 += '</svg>'

    print("--- DATEI 1: gabriel_skeleton.svg ---")
    print(svg1)
    print("\n--- DATEI 2: complexity_curve.svg ---")
    print(svg2)

generate_svg_outputs()