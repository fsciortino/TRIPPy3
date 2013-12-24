#include <math.h>

void intercept2d(double outval[], double pt1[3], double pt2[3], double outliner[], double outlinez[], int ix)
{ 
  /* initialize variables */
  int i;
  double delr,delz,del1,del2,denom;
  *outval = INFINITY;

  delr = pt1[0] - pt2[0];
  delz = pt1[2] - pt2[2];

  for(i= ix-1 ;i--;)
    {

      del1 = outliner[i+1]-outliner[i];
      del2 = outlinez[i+1]-outlinez[i];

      /* If the inverse is possible  */
      denom = delr*del2 - delz*del1;
      if(denom)
	{
	  del1 = (del2*(pt1[0] - outliner[i]) - del1*(pt1[2] - outlinez[i]))/denom;
	  del2 = (delr*(pt1[2] - outlinez[i]) - delz*(pt1[0] - outliner[i]))/denom;
	  /*Does the point intercept, and is it smaller than the previous smallest value?  */
	  /* del2 is the length between outline at point i+1 to point i where the intercept occurs */
	  /* del1 is the length between pt1 and pt2 where the intercept occurs */

	  if((del2 > 0) & (del2 < 1) & (del1 < *outval) & (del1 > 0))
	    { 
	      *outval = del1;
	    }
	}
    }
}