import matplotlib.pyplot as plt
from numpy import *

###List of variables
#	r_in		[10**10 cm]			innder radius
#	r_out		[10**10 cm]			outer radius
#	step		[10**10 cm]			step of plot
#	alfa		[]					parameter of accretion
#	M_16		[10**6 g.s**(-1)]	accretion flow
#	m_1			[solar mass]		mass of compact object
#	R_hv		[10**10 cm]			radius of compact object
#	R_10		[10**10 cm]			distance from compact object
#	f								numerical factor

###List of computed parameters
#	Surface density					[g.cm**(-2)]		(sigma)		
#	Height							[cm]				(H)
#	Density							[g.cm**(-3)]		(rho)
#	Central disc temeprature		[K]					(T_c)
#	Opacity							[]					(tau)
#	viscosity						[cm**2.s**(-1)]		(nu)
#	radial velocity towards center	[cm.s**(-1)]		(v_r)

###function solutions parameters
# 	parameter 1		r_in		
# 	parameter 2		r_out 		
# 	parameter 3		step		
# 	parameter 4		alfa		
# 	parameter 5		M_16		
# 	parameter 6		m_1
# 	parameter 7		R_hv


def solutions(r_in,r_out,step,alfa,M_16,m_1,R_hv):
	#defining lists
	list_function = arange(r_in,r_out,step)
	R_10_l,surface_density_l,height_l,density_l,Fx = ([] for i in range(5))
	temperature_l,opacity_l,viscosity_l,radial_velocity_l = ([] for i in range(4))
	#computation and appending to lists
	for R_10 in list_function:
		f=(1-((R_hv)/(R_10))**(1.0/2))**(1.0/4)
		surface_density = 5.2*alfa**(-4.0/5)*M_16**(7.0/10)*m_1**(1.0/4)*R_10**(-3.0/4)*f**(14.0/5)
		height =  1.7*10**8*alfa**(-1.0/10)*M_16**(3.0/20)*m_1**(-3.0/8)*R_10**(9.0/8)*f**(3.0/5)
		density = 3.1*10**(-8)*alfa**(-7.0/10)*M_16**(11.0/20)*m_1**(5.0/8)*R_10**(-15.0/8)*f**(11.0/5)
		temperature = 1.4*10**4*alfa**(-1.0/5)*M_16**(3.0/10)*m_1**(1.0/4)*R_10**(-3.0/4)*f**(6.0/5)
		opacity = 190*alfa**(-4.0/5)*M_16**(1.0/5)*f**(4.0/5)
		viscosity = 1.8*10**14*alfa**(4.0/5)*M_16**(3.0/10)*m_1**(-1.0/4)*R_10**(3.0/4)*f**(6.0/5)
		radial_velocity = 2.7*10**4*alfa**(4.0/5)*M_16**(3.0/10)*m_1**(-1.0/4)*R_10**(-1.0/4)*f**(-14.0/5)
		R_10_l.append(R_10)
		surface_density_l.append(surface_density)
		height_l.append(height)
		density_l.append(density)
		temperature_l.append(temperature)
		opacity_l.append(opacity)
		viscosity_l.append(viscosity)
		radial_velocity_l.append(radial_velocity)
		Fx.append(f)
	#transformation R_10 to kolimeters
	R_km = [ x / 10**(-4) for x in R_10_l]
	return R_km, surface_density_l, height_l, density_l,temperature_l,opacity_l,viscosity_l,radial_velocity_l,Fx

#for definitions of parameters look up
r_in =1.0001*10**(-4)
r_out =10**(-2)
step = 10**(-6)
alfa = 0.5
M_16 = 10
m_1 = 5
R_hv = 1.0*10**(-4)

lists=solutions(r_in,r_out,step,alfa,M_16,m_1,R_hv)

print 30*"-"
print "Used parameter values"
print 30*"-"
print "innder radius:", 10*".",r_in, 10*".", "[10$^{10}$ cm]"
print "outer radius:", 10*".", r_out, 10*".", "[10$^{10}$ cm]"
print "step of plot:", 10*".", step, 10*".", "[10$^{10}$ cm]"
print "parameter of accretion alfa:", 10*".", alfa
print "accretion flow:", 10*".", M_16, 10*".", "[10$^6$ g.s${-1)}$]"
print "mass of compact object:", 10*".", m_1, 10*".", "[solar mass]"
print "radius of compact object:", 10*".", R_hv, 10*".", "[10$^{10}$ cm]"



plt.plot(lists[0], lists[1])
plt.title('surface density')
plt.xlabel('radius [km]')
plt.ylabel('surface density [g.cm$^{-2}$] ')
plt.grid()
plt.savefig("surface density")
plt.gcf().clear()

plt.plot(lists[0], lists[2])
plt.title('height')
plt.xlabel('radius [km]')
plt.ylabel('height [cm] ')
plt.grid()
plt.savefig("height")
plt.gcf().clear()

plt.plot(lists[0], lists[3])
plt.title('density')
plt.xlabel('radius [km]')
plt.ylabel('density [g.cm$^{-3}$] ')
plt.grid()
plt.savefig("density")
plt.gcf().clear()

plt.plot(lists[0], lists[4])
plt.title('temperature')
plt.xlabel('radius [km]')
plt.ylabel('temperature [K] ')
plt.grid()
plt.savefig("temperature")
plt.gcf().clear()

plt.plot(lists[0], lists[5])
plt.title('opacity')
plt.xlabel('radius [km]')
plt.ylabel('opacity ')
plt.grid()
plt.savefig("opacity")
plt.gcf().clear()

plt.plot(lists[0], lists[6])
plt.title('viscosity')
plt.xlabel('radius [km]')
plt.ylabel('viscosity [cm$^{2}$.s$^{-1}$] ')
plt.grid()
plt.savefig("viscosity")
plt.gcf().clear()

plt.plot(lists[0], lists[7])
plt.title('radial velocity')
plt.xlabel('radius [km]')
plt.ylabel('radial velocity [cm.s$^{-1}$] ')
plt.grid()
plt.savefig("radial velocity")
plt.gcf().clear()
