import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def develop(): subprocess.run(['gatsby', 'develop'])
@cli.command()
def build(): subprocess.run(['gatsby', 'build'])
@cli.command()
def serve(): subprocess.run(['gatsby', 'serve'])
if __name__ == '__main__': cli()
