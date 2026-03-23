import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('leader running')
@cli.command()
def start(): click.echo('leader started')
if __name__ == '__main__': cli()
