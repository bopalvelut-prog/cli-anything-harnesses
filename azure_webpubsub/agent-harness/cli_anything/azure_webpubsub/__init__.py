import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('azure_webpubsub running')
@cli.command()
def start(): click.echo('azure_webpubsub started')
if __name__ == '__main__': cli()
