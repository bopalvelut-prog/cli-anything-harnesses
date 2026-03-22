import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def stake(): click.echo('Lido stake')
@cli.command()
def withdraw(): click.echo('Lido withdraw')
if __name__ == '__main__': cli()
