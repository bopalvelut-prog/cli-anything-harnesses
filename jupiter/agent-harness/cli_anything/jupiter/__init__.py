import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def swap(): click.echo('Jupiter swap')
@cli.command()
def route(): click.echo('Jupiter route')
if __name__ == '__main__': cli()
