public sealed class Singleton1  // sealed 是啥意思？
{
    private Singleton1(){}

    private static Singleton1 instance = null;
    public static Singleton1 Instance
    {
        get 
        {
            if (instance == null)
                instance = new Singleton1();
            
            return instance;
        }
    }

}