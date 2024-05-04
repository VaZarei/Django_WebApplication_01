def siteStaticVariabales(request):

    # HoomePage Content Layer 1

    parcontent1 = "Honing your programming skills is like building a muscle;consistent practice is key.<br> Here's how to make practice effective:Regular Coding: Dedicate time each day or week to actively writing code. Start with small exercises, work on personal projects, or participate in online coding challenges. This regular engagement keeps your coding muscles active and helps you learn new concepts faster.Focus on Problem-Solving: Don't just mindlessly code; approach problems critically. Analyze the requirements, break them down into smaller steps, and then code solutions. This problem-solving approach improves your ability to tackle complex challenges in the future.Embrace Challenges: Step outside your comfort zone. Try tackling problems that require you to learn new libraries, frameworks, or programming paradigms. This pushes your boundaries, broadens your skillset, and fosters resilience when facing difficulties."
    parcontent2 = "Effective learning fuels your programming journey. Here are some strategies to consider: Structured Learning: Supplement practice with structured learning. Take online courses, read programming books and tutorials, or watch video lectures from experts. These resources provide in-depth explanations, demonstrations, and exercises to solidify your understanding. Learning from Others: Actively engage with the programming community. Participate in online forums, attend coding meetups, or collaborate on open-source projects. This allows you to learn from others' experiences, ask questions, and gain valuable insights. Active Learning vs. Passive Consumption: Don't just passively consume information. Actively engage with learning material. Take notes, practice what you learn, and try to explain concepts to others. This active learning process helps retain information more effectively."
    parcontent3 = "As your skills grow, focus not just on functionality but also on writing clean and maintainable code. Here's why: Readability and Maintainability: Well-written code with clear structure, proper naming conventions, and comments is easier to understand and maintain for both you and others. This reduces the time and effort needed to modify or debug code in the future. Efficiency and Optimization: As you gain experience, strive to write efficient code that uses resources effectively. Consider performance optimizations and learn best practices for writing clean and concise code. Testing and Debugging: Develop good testing habits. Write unit tests to verify the functionality of your code and catch bugs early in the development process. Learn debugging techniques to efficiently troubleshoot issues when your code doesn't behave as expected. By incorporating these practices, you'll not only improve your programming skills but also write code that is robust, clear, and easier to work with in the long run."
    

    # HoomePage Content Layer 2

    context = {
        # Short Variables :

        "Site_Name" : "Code24",
        "Phone_Number": "+44-800-700-145",

        # HoomePage Content Layer 1
        
        "Column1_title"   : "Practice and Problem-Solving:" , 
        "Column1_content" : parcontent1,

        "Column2_title"   : "Learning Strategies and Resources:" , 
        "Column2_content" : parcontent2,

        "Column3_title"   : "Code Quality and Maintainability:" , 
        "Column3_content" : parcontent3,


        # HoomePage Content Layer 2




    }
    return context