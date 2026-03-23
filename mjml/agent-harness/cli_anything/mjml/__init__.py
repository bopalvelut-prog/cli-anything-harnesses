import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mjml running')
@cli.command()
def start(): click.echo('mjml started')
if __name__ == '__main__': cli()
