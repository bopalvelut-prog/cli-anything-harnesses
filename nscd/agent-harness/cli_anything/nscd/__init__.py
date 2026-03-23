import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nscd running')
@cli.command()
def start(): click.echo('nscd started')
if __name__ == '__main__': cli()
