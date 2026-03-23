import click
@click.group()
def cli(): pass
@cli.command()
def chat(): click.echo('Anthropic chat')
@cli.command()
def models(): click.echo('Anthropic models')
if __name__ == '__main__': cli()
