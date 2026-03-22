import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def beacon(): click.echo('Lodestar beacon')
@cli.command()
def validator(): click.echo('Lodestar validator')
if __name__ == '__main__': cli()
