import java.util.ArrayList;
import java.util.List;

interface Subscriber {
    void update(String issue);
}

class MagazinePublisher {
    private final List<Subscriber> subscribers = new ArrayList<>();

    public void addListener(Subscriber subscriber) {
        subscribers.add(subscriber);
    }

    public void notifyListeners(String issue) {
        for (Subscriber subscriber : subscribers) {
            subscriber.update(issue);
        }
    }
}

class EmailSubscriber implements Subscriber {
    public void update(String issue) {
        System.out.println("Email: new issue published — " + issue);
    }
}
