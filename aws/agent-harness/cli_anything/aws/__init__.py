import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def configure(): subprocess.run(['aws', 'configure'])
@cli.command()
def s3(): subprocess.run(['aws', 's3', 'ls'])
if __name__ == '__main__': cli()
