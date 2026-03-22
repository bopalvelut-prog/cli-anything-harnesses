import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('source')
@click.argument('dest')
def backup(source, dest): subprocess.run(['duplicity', source, dest])
@cli.command()
@click.argument('source')
@click.argument('dest')
def restore(source, dest): subprocess.run(['duplicity', 'restore', source, dest])
if __name__ == '__main__': cli()
