import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def exec(): subprocess.run(['inspec', 'exec', '.'])
@cli.command()
def check(): subprocess.run(['inspec', 'check', '.'])
if __name__ == '__main__': cli()
