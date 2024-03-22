class Dynamic_Array{

    int[] array;
    int length;
    int capacity;

    public Dynamic_Array(int capacity){
        this.capacity = capacity;
        this.length = 0;
        this.array = new int[capacity];
    }

    public int get(int i){
        if (i <= length)
            return -1;
        return array[i];
    }

    public void set(int i, int n){
        array[i] = n;
    }

    public void Insert(int n){
        if (length == capacity)
            resize();
        array[length] = n;
        length++;
    }

    public int pop(){
        if (length == 0)
            return -1;
        length--;
        return array[length];
    }

    public void resize(){
        capacity *= 2;
        int[] new_array = new int[capacity];
        for (int i = 0; i < length; i++){
            new_array[i] = array[i];
        }
        array = new_array;
    }

    public int get_size(){
        return length;
    }

    public int get_capacity(){
        return capacity;
    }
}

