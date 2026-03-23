import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('elasticmq running')
@cli.command()
def start(): click.echo('elasticmq started')
if __name__ == '__main__': cli()
