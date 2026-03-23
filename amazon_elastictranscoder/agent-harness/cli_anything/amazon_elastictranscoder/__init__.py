import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_elastictranscoder running')
@cli.command()
def start(): click.echo('amazon_elastictranscoder started')
if __name__ == '__main__': cli()
