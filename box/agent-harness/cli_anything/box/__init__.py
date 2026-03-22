import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def login(): click.echo('Box login')
@cli.command()
def files(): click.echo('Box files')
if __name__ == '__main__': cli()
