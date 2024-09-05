import os.path

from IPython.display import display, Image
from django.core.management.base import BaseCommand
from tasks.models import Task
from authentication.models import Profile
import pandas as pd
import matplotlib.pyplot as plt


class Command(BaseCommand):
    help = 'Analyze task completion rates and user productivity'

    def handle(self, *args, **kwargs):
        # Fetch data
        tasks = Task.objects.all().values()
        users = Profile.objects.all().values()

        # Analysis and visualization code
        self.perform_analysis(tasks, users)

    def perform_analysis(self, tasks, users):
        tasks_df = pd.DataFrame(tasks)
        users_df = pd.DataFrame(users)

        # Task completion rate
        completed_tasks = tasks_df[tasks_df['status'] == 'completed']
        completion_rate = len(completed_tasks) / len(tasks_df) * 100
        print(f"Overall Task Completion Rate: {completion_rate:.2f}%")

        # User productivity
        user_task_counts = completed_tasks['assigned_to_id'].value_counts()
        user_task_counts = user_task_counts.reset_index()
        user_task_counts.columns = ['user_id_x', 'tasks_completed']

        # Rename columns in user_task_counts before merging
        user_task_counts.rename(columns={'user_id_x': 'users_id'}, inplace=True)

        # Check columns in user_task_counts
        print(user_task_counts.columns)
        print(user_task_counts.dtypes)

        # Rename columns in user_task_counts before merging
        users_df.rename(columns={'id': 'users_id'}, inplace=True)

        # Check columns in users_df
        print(users_df.columns)
        print(users_df.dtypes)

        user_task_counts['users_id'] = user_task_counts['users_id'].astype(int)
        users_df['users_id'] = users_df['users_id'].astype(int)

        # Print unique values to verify common values
        print("Unique values in user_task_counts['users_id']:", user_task_counts['users_id'].unique())
        print("Unique values in users_df['users_id']:", users_df['users_id'].unique())

        user_productivity = pd.merge(user_task_counts, users_df, on='users_id')

        print(user_productivity.head())  # Empty data frame

        user_productivity = user_productivity[['users_id', 'tasks_completed']]
        print("User Productivity:\n", user_productivity)
        print(user_productivity.columns)

        # Display Results
        print('Completed Tasks DataFrame:\n', completed_tasks)
        print('\nUser Task Counts DataFrame:\n', user_task_counts)
        print('\nUser Productivity DataFrame:\n', user_productivity)

        # Save results to CSV
        user_productivity.to_csv('media/user_productivity.csv', index=False)

        # Visualization
        self.visualize_task_completion(completed_tasks, tasks_df)
        self.visualize_user_productivity(user_productivity)

        # Display saved images as a slideshow
        self.display_slideshow(['media/task_completion_rate.png', 'media/user_productivity.png'])


    def visualize_user_productivity(self, user_productivity):
        if user_productivity.empty:
            print('User Productivity DataFrame is empty.No plot will be generated')
            return

        user_productivity.plot(kind='bar', x='users_id', y='tasks_completed', legend=False, color='blue',
                               figsize=(10, 6))
        plt.title('User Productivity')
        plt.xlabel('User')
        plt.ylabel('Tasks Completed')
        plt.savefig('media/user_productivity.png')
        plt.show()
        plt.close()

    def visualize_task_completion(self, completed_tasks, tasks_df):
        plt.figure(figsize=(6, 4))
        plt.bar(['Completed', 'Pending'], [len(completed_tasks), len(tasks_df) - len(completed_tasks)],
                color=['green', 'red'])
        plt.title('Task Completion Status')
        plt.xlabel('Status')
        plt.ylabel('Number of Tasks')
        plt.savefig('media/task_completion_rate.png')
        plt.show()
        plt.close()

    def display_slideshow(self,image_paths):
        for image_path in image_paths:
            if os.path.exists(image_path):
                print(f'Displaying image:{image_path}')
                display(Image(filename=image_path))
            else:
                print(f'Image not found:{image_path}')
