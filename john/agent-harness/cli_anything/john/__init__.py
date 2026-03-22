import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('hash_file')
def crack(hash_file): subprocess.run(['john', hash_file])
@cli.command()
def show(): subprocess.run(['john', '--show'])
if __name__ == '__main__': cli()
