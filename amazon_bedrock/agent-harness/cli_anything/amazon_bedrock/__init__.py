import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_bedrock running')
@cli.command()
def start(): click.echo('amazon_bedrock started')
if __name__ == '__main__': cli()
