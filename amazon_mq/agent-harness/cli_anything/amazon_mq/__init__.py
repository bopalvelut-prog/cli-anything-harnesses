import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_mq running')
@cli.command()
def start(): click.echo('amazon_mq started')
if __name__ == '__main__': cli()
