import click
@click.group()
def cli(): pass
@cli.command()
def serve(): click.echo('vLLM serve')
@cli.command()
def models(): click.echo('vLLM models')
if __name__ == '__main__': cli()
