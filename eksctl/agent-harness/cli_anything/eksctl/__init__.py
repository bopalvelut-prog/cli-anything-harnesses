import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('eksctl running')
@cli.command()
def start(): click.echo('eksctl started')
if __name__ == '__main__': cli()
