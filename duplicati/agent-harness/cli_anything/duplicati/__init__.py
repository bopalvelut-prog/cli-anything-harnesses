import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def backup(): click.echo('Duplicati backup')
@cli.command()
def restore(): click.echo('Duplicati restore')
if __name__ == '__main__': cli()
