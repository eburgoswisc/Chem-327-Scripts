def get_dof_tscore(s1,s2,n1,n2):
	return (s1**2/n1 + s2**2/n2)**2 / ((s1**2/n1)**2/(n1-1) + (s2**2/n2)**2/(n2-1))