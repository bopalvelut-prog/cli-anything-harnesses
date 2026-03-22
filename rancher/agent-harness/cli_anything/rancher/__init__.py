import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def clusters(): click.echo('Rancher clusters')
@cli.command()
def login(): click.echo('Rancher login')
if __name__ == '__main__': cli()
