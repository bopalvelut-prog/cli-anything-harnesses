import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['luigi', '--module', 'my_module', 'MyTask'])
@cli.command()
def scheduler(): subprocess.run(['luigid'])
if __name__ == '__main__': cli()
