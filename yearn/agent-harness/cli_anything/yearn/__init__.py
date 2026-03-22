import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def vault(): click.echo('Yearn vault')
@cli.command()
def deposit(): click.echo('Yearn deposit')
if __name__ == '__main__': cli()
