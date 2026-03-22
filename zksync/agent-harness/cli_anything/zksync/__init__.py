import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def bridge(): click.echo('zkSync bridge')
@cli.command()
def transfer(): click.echo('zkSync transfer')
if __name__ == '__main__': cli()
