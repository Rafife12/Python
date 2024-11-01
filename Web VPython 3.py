Web VPython 3.2

h = 0,0
v0 = 42,0
θ0 = 60,0
g = 9,81
θ0_rad = radianos(θ0)

vx = v0 * cos(θ0_rad) vy = v0 * sin(θ0_rad)

projetil = esfera(pos=vetor(0, h, 0), raio=0,5, cor=cor.vermelho, make_trail=True)

trajetória = gcurve(cor=cor.azul)

t = 0 dt = 0,01

posicao = projetil.pos velocidade = vector(vx, vy, 0)

enquanto posicao.y >= h e t <= 5,50: taxa(100)

velocidade.y = velocidade.y - g * dt


posicao = posicao + velocidade * dt
projetil.pos = posicao


trajetoria.plot(posicao.x, posicao.y)


t = t + dt


print(f"Tempo: {t:.2f} s | Velocidade Horizontal: {velocidade.x:.2f} m/s | Velocidade Vertical: {velocidade.y:.2f} m/s | Posição Horizontal: {posicao.x:.2f} m | Posição Vertical: {posicao.y:.2f} m")
