import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('Hygraph login')
@cli.command()
def schema(): click.echo('Hygraph schema')
if __name__ == '__main__': cli()
