int findMax(struct Height arr[], int n)
{
    // Code here
    int val[n];
    int mx = 0;
    for(int i=0; i<n;i++){
        val[i] = arr[i].feet*12 + arr[i].inches;
        if (val[i] > mx)
        mx = val[i];
        
    }
    return mx;
    
}