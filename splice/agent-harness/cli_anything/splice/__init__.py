import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('splice running')
@cli.command()
def start(): click.echo('splice started')
if __name__ == '__main__': cli()
